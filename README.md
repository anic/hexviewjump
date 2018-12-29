# hexviewjump
Hexviewjump is an IDA 7.0 pro plugin. It helps to quickly jump to target memory address by double clicking the content from HexView, or by using complicated expression (eg. *rax).

## Installation
Installing the plugin is as simple as copying the files hewviewjump.py to the ```plugins\``` folder in your IDA installation directory.

## Use cases
- case 1 
double click the content as a pointer in the HexView, it will jump to the memory of that piointer.

- case 2 
press the shortcut G, input the expression of address (eg. rax,*rax). If ```rax``` is input, it will jump to the memory of rax as pointer, as the default function in JumpAsk. If ```*rax``` is input, it will get the content of rax first, use it as an pointer, and jump to the memory of that pointer. 

NOTE: 
- This plugin will replace the default JumpAsk of IDA.
- Only available in IDA 7.0 .