#!/usr/bin/env node

/**
 * Compile Ink Examples to JSON
 * 
 * This script compiles all .ink files in _examples/ to .json format
 * for use with the interactive ink-player component.
 * 
 * Uses inkjs compiler (npx inkjs)
 * 
 * Usage:
 *   node scripts/compile-examples.js
 *   node scripts/compile-examples.js chapter04/sticky-choices
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const EXAMPLES_DIR = path.join(__dirname, '..', '_examples');

// Find all .ink files recursively
function findInkFiles(dir) {
  const inkFiles = [];
  
  function scan(currentDir) {
    const items = fs.readdirSync(currentDir);
    
    for (const item of items) {
      const fullPath = path.join(currentDir, item);
      const stat = fs.statSync(fullPath);
      
      if (stat.isDirectory()) {
        scan(fullPath);
      } else if (item.endsWith('.ink')) {
        inkFiles.push(fullPath);
      }
    }
  }
  
  scan(dir);
  return inkFiles;
}

// Compile a single ink file
function compileInkFile(inkPath) {
  const relativePath = path.relative(EXAMPLES_DIR, inkPath);
  const tempJsonPath = inkPath + '.json';  // inkjs creates .ink.json
  const finalJsonPath = inkPath.replace(/\.ink$/, '.json');
  
  try {
    console.log(`📝 Compiling ${relativePath}...`);
    
    // Run inkjs compiler - it creates .ink.json
    execSync(`npx inkjs "${inkPath}"`, { stdio: 'pipe' });
    
    // Rename .ink.json to .json
    if (fs.existsSync(tempJsonPath)) {
      fs.renameSync(tempJsonPath, finalJsonPath);
      console.log(`✅ Created ${path.relative(EXAMPLES_DIR, finalJsonPath)}`);
      return true;
    } else {
      console.error(`❌ Expected output file not found: ${tempJsonPath}`);
      return false;
    }
  } catch (error) {
    console.error(`❌ Failed to compile ${relativePath}`);
    console.error(error.message);
    
    // Clean up temp file if it exists
    if (fs.existsSync(tempJsonPath)) {
      fs.unlinkSync(tempJsonPath);
    }
    
    return false;
  }
}

// Main function
function main() {
  console.log('🎨 Ink Examples Compiler\n');
  
  // Check if specific file was requested
  const args = process.argv.slice(2);
  let inkFiles = [];
  
  if (args.length > 0) {
    // Compile specific file(s)
    for (const arg of args) {
      const inkPath = path.join(EXAMPLES_DIR, arg.endsWith('.ink') ? arg : arg + '.ink');
      if (fs.existsSync(inkPath)) {
        inkFiles.push(inkPath);
      } else {
        console.error(`❌ File not found: ${arg}`);
      }
    }
  } else {
    // Compile all .ink files
    inkFiles = findInkFiles(EXAMPLES_DIR);
  }
  
  if (inkFiles.length === 0) {
    console.log('No .ink files found to compile.');
    return;
  }
  
  console.log(`Found ${inkFiles.length} file(s) to compile\n`);
  
  let succeeded = 0;
  let failed = 0;
  
  for (const inkFile of inkFiles) {
    if (compileInkFile(inkFile)) {
      succeeded++;
    } else {
      failed++;
    }
  }
  
  console.log(`\n📊 Summary:`);
  console.log(`   ✅ Succeeded: ${succeeded}`);
  console.log(`   ❌ Failed: ${failed}`);
  
  if (failed > 0) {
    process.exit(1);
  }
}

main();
