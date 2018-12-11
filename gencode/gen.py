#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

class Gen:

    def __init__(self,path,args):
        self.path= path
        self.args = args

    def write(self):
        self._clearDir()
        self._writeInterfaceTemplete()
        self._writeDalTemplete()
        self._writeBllTemplete()

    def _writeInterfaceTemplete(self):
        s = """ 
        namespace HXYX.DataCenter.IDal.Report
        {
            public interface I$_Dal
            {

            }
        }
            """
        arg1 = self.args[1]
        f_name = "I" + arg1 + "Dal.cs"
        f_path = os.path.join(self.path, f_name)
        self._writeFile(f_path, s.replace("$_", arg1))

    def _writeDalTemplete(self):
        s = """
        using HXYX.DataCenter.Domain.Model;
        using HXYX.DataCenter.IDal.Report;

        namespace HXYX.DataCenter.Dal.Report
        {
            public class $_Dal : DalBase<$$>, I$_Dal
            {

            }
        }
            """

        arg1 = self.args[1]
        arg2 = self.args[2]
        f_name = arg1 + "Dal.cs"
        f_path = os.path.join(self.path, f_name)
        self._writeFile(f_path, s.replace("$_", arg1).replace("$$", arg2))

    def _writeBllTemplete(self):
        s = """
        using HXYX.DataCenter.Dal;
        using HXYX.DataCenter.Domain.Model;
        using HXYX.DataCenter.IDal.Report;

        namespace HXYX.DataCenter.BLL.Report
        {
            public class $_Bll
            {
                private I$_Dal $$Dal;

                protected I$_Dal $_Dal
                {
                    get
                    {
                        if ($$Dal == null)
                        {
                            $$Dal = DalFactory.GetInstance<I$_Dal>();
                        }

                        return $$Dal;
                    }
                }
            }
        }
            """
        arg1 = self.args[1]
        arg3 = self.args[3]

        f_name = arg1 + "Bll.cs"
        f_path = os.path.join(self.path, f_name)
        self._writeFile(f_path, s.replace("$_", arg1).replace("$$", arg3))

    def _writeFile(self,p,s):
        f = open(p, 'w')
        f.write(s)
        f.close()

    def _clearDir(self):
        p =self.path
        fl = os.listdir(p)
        for i in fl:
            c_path = os.path.join(p, i)
            os.remove(c_path)