# filename: hewviewjump.py
# -*- coding: UTF-8 -*-
# 原作者：sonnzy，修改者：anic
import idaapi
from ida_kernwin import *
from idc import *

class HexViewjumpPlugin(idaapi.plugin_t):
	flags = idaapi.PLUGIN_FIX
	comment = "hewview jump t0 addresss"
	help = "hewview jump"
	wanted_name = "hewview jump "
	wanted_hotkey = "Ctrl+G"  #override G shortcut
	index = 1

	def init(self):	  
		msg("[hewview jump] hewview jump plugin hooked \n")
		global myviewhook #必须加global,否则这个无法生效
		myviewhook = MyViewHook()
		myviewhook.hook()
		return idaapi.PLUGIN_KEEP

	def term(self):
		pass
	 

	def run(self, arg):
		saddr = ask_str("", 0, "Jump address(Extend)")
		if saddr is None:
			return

		#获取表达式对应的地址值
		addr = str2ea(saddr)
		#先尝试一次Jump
		if Jump(addr):
			return
		
		#如果有*号开头
		if "*" == saddr[0]:
			#判断是32位还是64位
			info = idaapi.get_inf_structure() 
			get_addr = Qword if info.is_64bit() else Dword
		
			#取星号后的内容
			addr = str2ea(saddr[1:])
			msg("[jump ask extend] %s : %s \n"%(saddr[1:],hex(addr)))
			addr = get_addr(addr)
			msg("[jump ask extend] *%s : %s \n"%(saddr[1:],hex(addr)))
			Jump(addr)


class MyViewHook(View_Hooks):
	def __init__(self):
		View_Hooks.__init__(self)
		
	def view_dblclick(self, *args):
		v= args[0]
		if(get_widget_type(v) == ida_kernwin.BWN_DUMP):
			#判断是32位还是64位
			info = idaapi.get_inf_structure() 
			get_addr = Qword if info.is_64bit() else Dword
			
			if(not Jump(get_addr(ScreenEA()))):
				Message("[hewview jump] Jump fail\n")
		View_Hooks.view_dblclick(self, *args)

def PLUGIN_ENTRY():
	return HexViewjumpPlugin()
