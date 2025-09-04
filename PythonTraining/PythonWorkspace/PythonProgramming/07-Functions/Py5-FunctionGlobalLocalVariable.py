#global Variable
x = 100

def show_local():
    #local variable
    x = 10
    print("Inside show_local (local x):", x)

def show_global():
    #showing the global_variable
    print("Inside show_global (global x):", x)

def modify_global():
    global x #Tells python to use the global variable
    x = x + 50
    print("Inside modify_global (global x):", x)

show_local()
show_global()
modify_global()