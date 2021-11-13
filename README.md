#整体结构目录说明

**api：api封装包**

**common：通用方法的封装**
* baseapi：api对象的基类封装
* readconfig：读取config.ini文件

**config：目录管理**
* conf：目录管理
* config.ini：存放环境链接等配置数据

**data**
* request_data：将api请求数据以yaml文件的形式存放在该目录
* test_data：测试数据存放目录

**logs：存放日志文件**

**report：存放测试报告**

**test_case：测试用例封装包**

**utils：第三方工具类的封装包**
* utils_config：ini配置文件相关方法封装
* utils_logger：logging日志的封装
* utils_time：time与datetime相关方法的封装
* utils_yaml：yaml文件相关方法封装

**pytest.ini：pytest的配置文件**

**run_case.py：测试用例运行主入口**