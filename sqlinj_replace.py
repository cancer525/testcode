def qn(s):  
	dirty_stuff = ["\"", "\\", "/", "*", "'", "=", "-", "#", ";", "<", ">", "+", "%"]  
	for stuff in dirty_stuff:  
		s = s.replace(stuff,"")  

	return "'"+s+"'" 

def get_user_main_menus(request,md_code):  
	sql = "parent_id in (SELECT id FROM t_Menu WHERE module_code = "+qn(md_code)+")"  
	objs = Menu.objects.extra(sql)  
	#objs = Menu.objects.extra(where=[sql])  

get_user_main_menus("", request.GET[1])	      
