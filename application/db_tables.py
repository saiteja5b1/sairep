import psycopg2

class table:
    def __init__(self,conn,username):
        """ initilization of db instance """
        self.connection=conn
        self.user_name=username
        
    def user_personal_details(self,args): 
        """ table for storing user personal details """ 

        self.command=""" 
        insert into user_personal_details(fullname,age,phonenumber,adress,state,district,mandal,username) values(%s,%s,%s,%s,%s,%s,%s,%s);
        """
        try:
            print(args)
            self.cur=self.connection.cursor()
            self.cur.execute(self.command,(args[0],args[1],args[2],args[3],args[4],args[5],args[6],self.user_name))
            self.connection.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            return(error)
        finally:
            if self.connection is not None:
                self.connection.close()
                return("success")

    def user_login_credentials(self,args):
        """ table for storing the user credentialls """

        self.command="""
        insert into user_login_credentials(username,password) values(%s,%s);
        """
        try:
            self.cur=self.connection.cursor()
            self.cur.execute(self.command,(self.user_name,args[0]))
            self.connection.commit()


        except (Exception, psycopg2.DatabaseError) as error:
            return(error)
        finally:
            if self.connection is not None:
                self.connection.close()
                return("success")

    def user_agro_details(self,args):
        """ table for storing user agro details """

        self.command="""insert into user_agro_details(username,land,placeofland,landtype) values(%s,%s,%s,%s);"""

        try:
            print(self.connection)
            self.cur=self.connection.cursor()
            self.cur.execute(self.command,(self.user_name,args[0],args[1],args[2]))
            self.connection.commit()


        except (Exception, psycopg2.DatabaseError) as error:
            return(error)
        finally:
            if self.connection is not None:
                self.connection.close()
                return("success")
    
 

    def get_details(self):
        """ table for storing user agro details """
        self.command="""
        select type,crop from crops;       
        """
        try:
            self.cur=self.connection.cursor()
            self.cur.execute(self.command)
            data=self.cur.fetchall()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.connection is not None:
                self.connection.close()
                return(data)