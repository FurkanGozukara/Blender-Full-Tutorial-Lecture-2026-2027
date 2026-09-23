// Optional PNG regeneration: install Node.js, then npm install sharp in this folder.
const path = require('path');
const sharp = require('sharp');
const root = path.join(__dirname, 'reference');
(async () => {
  for (const name of ['housing_reference','housing_front','housing_side_section']) {
    await sharp(path.join(root,name+'.svg')).png().toFile(path.join(root,name+'.png'));
    console.log(name+'.png');
  }
})().catch(e=>{console.error(e);process.exitCode=1;});
