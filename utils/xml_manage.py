#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 上午10:15
# @Author  : huanghe
# @Site    : 
# @File    : xml_manage.py
# @Software: PyCharm
from xml.etree.ElementTree import ElementTree,Element
from utils.path_manage import Path
from xml.dom import minidom
import os


class XmlManage:

    def __init__(self, filename=None):
        self.filename = Path().get_xml_path(filename)

    @staticmethod
    def open_xml(filename):
        tree = ElementTree()
        tree.parse(filename)
        return tree

    @staticmethod
    def save(tree,outfile):
        tree.write(outfile, encoding="utf-8",xml_declaration=True)

    @staticmethod
    def add_child_node(nodelist, element):
        '''给一个节点添加子节点
           nodelist: 节点列表
           element: 子节点'''
        for node in nodelist:
            node.append(element)

    @staticmethod
    def del_node_by_tagkeyvalue(nodelist, tag, kv_map):
        '''同过属性及属性值定位一个节点，并删除之
           nodelist: 父节点列表
           tag:子节点标签
           kv_map: 属性及属性值列表'''
        for parent_node in nodelist:
            children = parent_node.getchildren()
            for child in children:
                if child.tag == tag and XmlManage.if_match(child, kv_map):
                    parent_node.remove(child)

    @staticmethod
    def create_node(tag, property_map, content=''):
        '''新造一个节点
           tag:节点标签
           property_map:属性及属性值map
           content: 节点闭合标签里的文本内容
           return 新节点'''
        element = Element(tag, property_map)
        element.text = content
        return element

    @staticmethod
    def change_node_text(nodelist, text, is_add=False, is_delete=False):
        '''改变/增加/删除一个节点的文本
           nodelist:节点列表
           text : 更新后的文本'''
        for node in nodelist:
            if is_add:
                node.text += text
            elif is_delete:
                node.text = ""
            else:
                node.text = text

    @staticmethod
    def change_node_properties(nodelist, kv_map, is_delete=False):
        '''修改/增加 /删除 节点的属性及属性值
           nodelist: 节点列表
           kv_map:属性及属性值map'''
        for node in nodelist:
            for key in kv_map:
                if is_delete:
                    if key in node.attrib:
                        del node.attrib[key]
                else:
                    node.set(key, kv_map.get(key))

    @staticmethod
    def get_node_by_keyvalue(nodelist, kv_map):
        '''根据属性及属性值定位符合的节点，返回节点
           nodelist: 节点列表
           kv_map: 匹配属性及属性值map'''
        result_nodes = []
        for node in nodelist:
            if XmlManage.if_match(node, kv_map):
                result_nodes.append(node)
        return result_nodes

    @staticmethod
    def find_nodes(tree, path):
        '''查找某个路径匹配的所有节点
           tree: xml树
           path: 节点路径'''
        return tree.findall(path)

    @staticmethod
    def if_match(node, kv_map):
        '''判断某个节点是否包含所有传入参数属性
           node: 节点
           kv_map: 属性及属性值组成的map'''
        for key in kv_map:
            if node.get(key) != kv_map.get(key):
                return False
        return True

    # 获取节点属性
    def get_value_by_name(self, name):
        tree = XmlManage.open_xml(self.filename)
        if tree is None:
            return None
        nodes = XmlManage.find_nodes(tree, 'date')
        nodes = XmlManage.get_node_by_keyvalue(nodes, {'name': name})
        if len(nodes) > 0:
            return nodes[0].attrib['value']
        return None

    # 设置节点
    def set_value_by_name(self, name, value):
        tree = XmlManage.open_xml(self.filename)
        if tree is None:
            return None
        nodes = XmlManage.find_nodes(tree, 'date')
        nodes = XmlManage.get_node_by_keyvalue(nodes, {'name': name})
        if len(nodes) > 0:
            nodes[0].attrib['value'] = value
            XmlManage.save(tree, self.filename)

    # 添加节点
    def add_tage(self, name, value):
        tree = XmlManage.open_xml(self.filename)
        XmlManage.add_child_node([tree.getroot()], XmlManage.create_node('date', {'name': name, 'value': value}))
        XmlManage.save(tree, self.filename)

    # 删除节点
    def de_tag_by_name(self, name):
        tree = XmlManage.open_xml(self.filename)
        XmlManage.del_node_by_tagkeyvalue([tree.getroot()], 'date', {'name': name})
        XmlManage.save(tree, self.filename)

    def create_xml(self,data):
        impl = minidom.getDOMImplementation()
        doc = impl.createDocument(None, None, None)
        rootElement = doc.createElement('dates')
        for key, value in data.items():
            # 创建子元素
            childElement = doc.createElement('date')
            # 为子元素添加id属性
            childElement.setAttribute('name', str(key))
            childElement.setAttribute('value', str(value))
            # 将子元素追加到根元素中
            rootElement.appendChild(childElement)
            # 将拼接好的根元素追加到dom对象
            doc.appendChild(rootElement)
            # 打开test.xml文件 准备写入
        f = open(self.filename, 'w', encoding='UTF-8')
        # 清空数据
        f.seek(0)
        f.truncate()
        # 写入文件
        doc.writexml(f, addindent=' ', newl='\n', encoding='UTF-8')
        # 关闭
        f.close()


if __name__ == '__main__':
    xmlmanage = XmlManage(filename='test01.xml')
    data = {"name":"张三"}
    xmlmanage.create_xml(data)
