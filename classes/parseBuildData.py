class ParseBuildData():
    build=[]
    helm=[]
    details=[]
    securityTest=[]

    def __init__(self) -> None:
        pass
       
    def test(self):
        print("İmage build edilmiş")

    def parseDevops(self,value ):
        class_parse_json_data=ParseBuildData()
        if type(value) == type(dict()):
                        class_parse_json_data.ArrayCreation(value)      
        elif type(value) == type(list()):
                for val in value:
                        if type(val) == type(str()):
                                pass
                        elif type(val) == type(list()):
                                    pass
                        else:
                                class_parse_json_data.ArrayCreation(val)
        return(value)   

    def ArrayCreation(self, data):
            class_parse_json_data=ParseBuildData()

            for key,value in data.items():
                    if(str(key)=='build'):
                            self.build.append(class_parse_json_data.parseDevops(value))
                    elif (str(key)=='details') :
                            self.details.append(class_parse_json_data.parseDevops(value))
                    elif (str(key)=='SecurityTest') :
                            self.securityTest.append(class_parse_json_data.parseDevops(value))
                    elif (str(key)=='helm') :
                            self.helm.append(class_parse_json_data.parseDevops(value))