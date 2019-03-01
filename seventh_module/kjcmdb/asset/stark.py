# -*- coding: utf-8 -*-

# __title__ = 'stark.py'
# __author__ = 'YangYang'
# __mtime__ = '2019.03.01'


from stark.service.v1 import site
from asset import models


from asset.views.depart  import DepartmentHandler
from asset.views.userinfo  import UserInfoHandler
from asset.views.machine  import MachineHandler
from asset.views.employee_department  import EmployeeDepartmentHandler
from asset.views.employee import EmployeeHandler
from asset.views.fix_phone import FixPhoneHandler
from asset.views.deploy_service import DeployServiceHandler
from asset.views.office_equipment import OfficeEquipmentHandler
# 部门管理
site.registry(models.Department,DepartmentHandler)
# 用户管理
site.registry(models.UserInfo,UserInfoHandler)
# 本地虚拟机管理
site.registry(models.Machine,MachineHandler)

# 员工部门管理
site.registry(models.EmployeeDepartment,EmployeeDepartmentHandler)
# 员工管理
site.registry(models.Employee,EmployeeHandler)

# 固定电话
site.registry(models.FixPhone,FixPhoneHandler)

# 部署服务地址
site.registry(models.DeployService,DeployServiceHandler)

# 办公资产
site.registry(models.OfficeEquipment,OfficeEquipmentHandler)



