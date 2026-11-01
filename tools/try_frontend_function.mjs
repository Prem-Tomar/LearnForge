// Calls the owned project function with the issue's small, visible examples.
import { readFile } from "node:fs/promises";
import { fileURLToPath, pathToFileURL } from "node:url";
import { dirname, resolve } from "node:path";
import { inspect } from "node:util";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const owners = { "web-study": "PratikTalware26", "web-knowledge": "praadeep28101995", "mobile-study": "bitsnbyt3s" };
const [feature, lesson = "J01"] = process.argv.slice(2);
if (!owners[feature] || !/^J0[1-7]$/.test(lesson)) {
  console.error("Use: node tools/try_frontend_function.mjs web-study|web-knowledge|mobile-study J01..J07");
  process.exit(2);
}

const plans = JSON.parse(await readFile(resolve(root, `curriculum/frontend-blueprints/${owners[feature]}.json`), "utf8"));
const task = plans.find(row => row.lesson === lesson);
const names = [...task.units.matchAll(/([A-Za-z_$][\w$]*)\(/g)].map(match => match[1]);
let module;
try {
  module = await import(pathToFileURL(resolve(root, task.files[0])).href);
} catch (error) {
  console.error(`Create/complete ${task.files[0]} as described in your issue. ${error.message}`);
  process.exit(2);
}
for (const name of names) {
  if (typeof module[name] !== "function") {
    console.error(`Export the named function ${name} from ${task.files[0]}.`);
    process.exit(2);
  }
}
const call = async (name, ...args) => {
  try {
    const result = await module[name](...args);
    console.log(`${name}(${args.map(a => inspect(a, { depth: 3, colors: false })).join(", ")}) -> ${inspect(result, { depth: 4, colors: false })}`);
    return result;
  } catch (error) {
    console.log(`${name}: ${error.name}: ${error.message}`);
    return undefined;
  }
};

const [first, second] = names;
if (lesson === "J01") {
  await call(first, { id: "s1", minutes: 0 });
  await call(first, { id: "s2", minutes: 15 });
} else if (lesson === "J02") {
  const a = await call(first);
  const b = await call(first);
  if (typeof a === "function" && typeof b === "function") console.log("a(), a(), b() ->", a(), a(), b());
} else if (lesson === "J03") {
  for (const value of ["0", "15", "", -1, NaN, Infinity, null, false]) await call(first, value);
} else if (lesson === "J04") {
  const records = [{ id: "s1", minutes: 30 }];
  const next = await call(first, records, { id: "s2", minutes: 15 });
  console.log("Original records after add:", inspect(records));
  if (next) await call(second, next);
  await call(second, []);
  await call(first, records, { id: "s1", minutes: 5 });
} else if (lesson === "J05") {
  await call(first, { id: "s1", minutes: 30 });
  await call(first, { id: "s2", minutes: 0 });
} else if (lesson === "J06") {
  await call(first, '[{"id":"s1","minutes":30}]');
  await call(first, "{");
  await call(first, '[{"id":"s1","minutes":"many"}]');
} else if (lesson === "J07") {
  await call(first, async () => '[{"id":"s1","minutes":30}]');
  await call(first, async () => { throw new Error("offline"); });
  await call(first, async () => "{");
}
