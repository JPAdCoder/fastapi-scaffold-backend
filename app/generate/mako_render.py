# coding=utf-8
"""
Time 2022-7-8 15:57
Author AdCoder
Email 17647309108@163.com
"""
from mako.template import Template
from datetime import datetime
from loguru import logger
import platform
import json


@logger.catch
def get_generate_json_params(json_path: str = "../statics/json/mako_model.json"):
    """
    根据路径将json文件转为dict
    """
    with open(json_path, "r", encoding="utf-8") as f:
        json_data = json.load(f)
    return json_data


@logger.catch
def get_replace_newline_syc():
    """
    根据操作系统类型返回要替换的换行符号
    """
    if platform.system() == 'Windows':
        return "\n"
    elif platform.system() == 'Linux':
        return "\r\n"
    else:
        # 除Win和Linux之外当MacOS
        return "\r"


@logger.catch
def render_py(t_path: str, json_path: str, model_py_path: str):
    """
    根据mako模板和json生成py文件
    """
    t = Template(filename=t_path)
    model_params = get_generate_json_params(json_path)
    with open(model_py_path, "w", encoding="utf-8") as f:
        content = t.render(**model_params, time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")) \
            .replace("\r\n", get_replace_newline_syc())
        f.write(content)
    return model_py_path


if __name__ == '__main__':
    # # land
    # # model
    # render_py("model.mako",
    #           "../statics/json/mako_model_land.json",
    #           "../project/mako_project/app/models/model_land.py")
    # # schema
    # render_py("schema.mako",
    #           "../statics/json/mako_schema_land.json",
    #           "../project/mako_project/app/schemas/schema_land.py")
    # # crud
    # render_py("crud.mako",
    #           "../statics/json/mako_crud_land.json",
    #           "../project/mako_project/app/crud/crud_land.py")

    # group_purchase
    # model
    # render_py("model.mako",
    #           "../statics/json/mako_model_group_purchase.json",
    #           "../project/mako_project/app/models/model_group_purchase.py")
    # schema
    render_py("../mako_scripts/schema.mako",
              "../statics/json/mako_schema_group_purchase.json",
              "../project/mako_project/app/schemas/schema_group_purchase.py")
    # crud
    # render_py("crud.mako",
    #           "../statics/json/mako_crud_group_purchase.json",
    #           "../project/mako_project/app/crud/crud_group_purchase.py")

    # extend_file
    # model
    # render_py("model.mako",
    #           "../statics/json/mako_model_extend_file.json",
    #           "../project/mako_project/app/models/model_extend_file.py")
    # schema
    # render_py("schema.mako",
    #           "../statics/json/mako_schema_extend_file.json",
    #           "../project/mako_project/app/schemas/schema_extend_file.py")
    # crud
    # render_py("crud.mako",
    #           "../statics/json/mako_crud_extend_file.json",
    #           "../project/mako_project/app/crud/crud_extend_file.py")
