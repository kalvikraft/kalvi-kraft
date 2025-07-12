const fs = require('fs');
const path = require('path');

function buildJSON(folder) {
  const fullPath = path.join(__dirname, '../../', folder);
  const files = fs.readdirSync(fullPath).filter(f => f.endsWith('.pdf'));

  const json = files.map(name => ({
    name: name.replace(/[-_]/g, ' ').replace('.pdf', ''),
    url: `https://raw.githubusercontent.com/kalvikraft/kalvi-kraft/main/${folder}/${name}`,
    subject: "",
    university: "KMC"
  }));

  return json;
}

const materials = buildJSON('study-materials');
const qps = buildJSON('old-question-papers');

fs.writeFileSync('json/materials.json', JSON.stringify(materials, null, 2));
fs.writeFileSync('json/old-qps.json', JSON.stringify(qps, null, 2));

console.log("✅ JSON files updated.");
