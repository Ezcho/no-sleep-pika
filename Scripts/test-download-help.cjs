const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
let shown = 0;
const dialogs = [];
function element(tag) {
  return {tag,style:{},children:[],handlers:{},open:false,
    setAttribute(){},appendChild(child){this.children.push(child);},
    addEventListener(name, fn){this.handlers[name]=fn;},
    showModal(){this.open=true;shown++;},close(){this.open=false;}};
}
const download=element('a');download.href='https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg';
const other=element('a');other.href='https://no-sleep-pika.online/install/ko/';
const document={documentElement:{lang:'ko'},querySelectorAll:()=>[download,other],getElementById:()=>null,
  createElement(tag){const el=element(tag);if(tag==='dialog')dialogs.push(el);return el;},body:element('body')};
vm.runInNewContext(fs.readFileSync('docs/downloads.js','utf8'),{document,location:{href:'https://no-sleep-pika.online/ko/'},URL});
assert.equal(shown,0,'page load must not show installation instructions');
assert.equal(other.handlers.click,undefined,'help/navigation links must not trigger instructions');
download.handlers.click({button:0,metaKey:true});assert.equal(shown,0);
download.handlers.click({button:0});assert.equal(shown,1);assert.equal(download.target,'_blank');
assert.equal(dialogs[0].children[0].textContent,'PKG가 열리지 않나요?');
assert.equal(dialogs[0].children.find(e=>e.tag==='ol').children.length,3);
dialogs[0].children.find(e=>e.tag==='button').handlers.click();assert.equal(dialogs[0].open,false);
download.handlers.click({button:0});assert.equal(shown,2);assert.equal(dialogs.length,1);
console.log('PASS download help: no automatic popup, download clicks only, dismiss and reopen, one dialog, three permission steps');
