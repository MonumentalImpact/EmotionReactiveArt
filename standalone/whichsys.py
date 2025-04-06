def whichsys():
    import os
    if 'uname' in dir(os):
        return(os.uname().sysname)
    else:
        import platform
        return( platform.uname().system )
        
if __name__ == '__main__':
    print(f"system is {whichsys()}")
