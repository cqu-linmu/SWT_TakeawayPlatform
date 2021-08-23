from application import app,manager
from flask_script import Server
from api.finance.Finance import route_finance
from api.stat.Stat import route_stat

#host需修改为服务器ip
manager.add_command( "runserver", Server( host='0.0.0.0',port=5111,use_debugger = True ,use_reloader = True) )
app.register_blueprint( route_finance,url_prefix = "/finance" )
app.register_blueprint( route_stat,url_prefix = "/stat" )

def main():
    manager.run( )

if __name__ == '__main__':
    try:
        import sys
        sys.exit( main() )
    except Exception as e:
        import traceback
        traceback.print_exc()