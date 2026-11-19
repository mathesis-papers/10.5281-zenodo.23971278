/* 六个镜头围绕同一证明机制：输入、规则、赋值、尾部、首个短距、结尾。 */
'use strict';
function heading(en, zh, a=1) {
  txt(en, W/2, 225, {size:48, fam:F.disp, w:700, align:'center', c:C.white, a});
  txt(zh, W/2, 285, {size:32, fam:F.zh, align:'center', c:C.dim, a});
}
function binaryRow(word, x, y, a=1, focus=-1) {
  const cell=100;
  [...word].forEach((b,i)=>{
    const col=i===focus?C.now:(b==='1'?C.cyan:C.dim);
    chip(x+i*cell,y,82,90,b,col,a,56,F.mono);
    txt(String(word.length-1-i),x+i*cell+41,y+132,{size:22,fam:F.mono,align:'center',c:C.dim,a});
  });
}
function questionArt(a=1) {
  panel(130,350,760,380,a,C.cyan,'n = 9');
  panel(1030,350,760,380,a,C.cyan,'n = 17');
  binaryRow('1001',310,450,a);
  binaryRow('10001',1160,450,a);
  txt('2 zeros  →  EVEN',510,680,{size:34,fam:F.disp,align:'center',c:C.white,a});
  txt('3 zeros  →  ODD',1410,680,{size:34,fam:F.disp,align:'center',c:C.white,a});
}
SCENES.question = S => {
  const a=clamp(S.u/0.8);
  heading('One missing zero','一个零的差别',a);
  questionArt(a);
  const b=at(S,2,0.8);
  txt('a(n) = (15n)! (2n)! / [(10n)! (6n)! n!]',W/2,820,
    {size:34,fam:F.mono,align:'center',c:C.cyan,a:b});
};
SCENES.rule = S => {
  badgeQ(S,[[0,null,'lean']]);
  heading('Three zeros decide parity','三个零决定奇偶性');
  binaryRow('100010001',515,380,1,8-Math.min(8,Math.floor(S.p*9)));
  panel(260,620,1400,200,1,C.cyan,'FOR EVERY n ≥ 0');
  txt('a(n) is a natural number',960,695,{size:40,fam:F.disp,align:'center',c:C.white});
  txt('ODD  ⇔  occupied positions differ by at least 4',960,765,
    {size:34,fam:F.disp,align:'center',c:C.white});
  txt('n = 0:  empty support;  a(0) = 1',960,875,
    {size:26,fam:F.mono,align:'center',c:C.dim,a:at(S,2,0.6)});
};
SCENES.valuation = S => {
  badgeQ(S,[[0,null,'argued']]);
  heading('Count factors, not huge products','数因子，不展开巨大乘积');
  panel(170,355,1580,205,1,C.cyan,'FLOOR DIFFERENCE');
  txt('F(x) = ⌊15x⌋ + ⌊2x⌋',960,435,{size:44,fam:F.math,align:'center',c:C.white});
  txt('− ⌊10x⌋ − ⌊6x⌋ − ⌊x⌋',960,505,{size:44,fam:F.math,align:'center',c:C.white});
  const a=at(S,1,0.8);
  [2,4,8,16,32].forEach((q,i)=>{
    chip(260+i*290,630,240,95,'F(n/'+q+')',C.cyan,a,30,F.mono);
    if(i<4)txt('+',530+i*290,690,{size:36,fam:F.math,c:C.dim,a});
  });
  txt('Each term: 0 or 1.   Odd ⇔ every term is 0.',960,820,
    {size:38,fam:F.disp,align:'center',c:C.white,a:at(S,2,0.7)});
};
SCENES.tail = S => {
  badgeQ(S,[[0,null,'argued']]);
  heading('A strict geometric bound','严格的几何级数界');
  panel(150,350,940,480,1,C.cyan,'SPACED LOWER BITS');
  const a=at(S,0,0.9);
  binaryRow('100010001',185,450,a);
  txt('2^e    2^(e−4)    2^(e−8)  …',620,700,
    {size:28,fam:F.mono,align:'center',c:C.dim,a});
  panel(1150,350,620,480,1,C.cyan,'TAIL / HIGHEST BIT');
  txt('R / 2^e',1460,445,{size:42,fam:F.math,align:'center',c:C.white});
  txt('< 1/16 + 1/16² + …',1460,545,{size:36,fam:F.math,align:'center',c:C.cyan,a:at(S,1,0.7)});
  txt('= 1/15',1460,640,{size:56,fam:F.math,align:'center',c:C.white,a:at(S,1,0.7)});
  txt('Every suffix gives F = 0',1460,750,{size:29,fam:F.disp,align:'center',c:C.white,a:at(S,2,0.7)});
};
function floorPanel(x,y,w,label,values,result,a=1) {
  panel(x,y,w,400,a,C.cyan,label);
  const cx=x+w/2;
  txt('⌊15x⌋  ⌊2x⌋  ⌊10x⌋  ⌊6x⌋  ⌊x⌋',cx,y+120,
    {size:26,fam:F.math,align:'center',c:C.dim,a});
  txt(values,cx,y+215,{size:42,fam:F.mono,align:'center',c:C.white,a});
  txt('F(x) = '+result,cx,y+320,{size:54,fam:F.math,align:'center',c:C.cyan,a});
}
SCENES.collision = S => {
  badgeQ(S,[[0,null,'argued'],[2,null,'computed']]);
  heading('The first short gap forces a 1','第一对过近的位，强制出现一个 1');
  const a=at(S,0,0.7);
  floorPanel(130,360,760,'n = 9;  x = 9/16','8 + 1 − 5 − 3 − 0',1,a);
  floorPanel(1030,360,760,'n = 17;  x = 17/32','7 + 1 − 5 − 3 − 0',0,at(S,1,0.7));
  txt('One positive term + all others ≥ 0  ⇒  EVEN',960,850,
    {size:36,fam:F.disp,align:'center',c:C.white,a:at(S,1,0.6)});
};
SCENES.close = S => {
  badgeQ(S,[[0,null,'lean'],[1,null,'argued']]);
  heading('A huge quotient, a short rule','巨大的阶乘商，简短的数字规则');
  binaryRow('10001',710,365,1);
  txt('At least 3 zeros  ⇔  odd a(n)',960,595,{size:48,fam:F.disp,align:'center',c:C.white});
  txt('Haobo Ma · Wenlin Zhang',960,675,{size:32,fam:F.disp,align:'center',c:C.cyan});
  txt('Version 4 · DOI: 10.5281/zenodo.23971279',960,735,{size:26,fam:F.mono,align:'center',c:C.dim});
  txt('Counting · bitwise identities · product divisibility',960,810,
    {size:32,fam:F.disp,align:'center',c:C.white,a:at(S,1,0.7)});
};
FILM.poster = () => {
  heading('Three zeros decide parity','三个零决定奇偶性');
  questionArt(1);
  txt('Haobo Ma · Wenlin Zhang  |  A295462',960,825,
    {size:30,fam:F.disp,align:'center',c:C.dim});
};
