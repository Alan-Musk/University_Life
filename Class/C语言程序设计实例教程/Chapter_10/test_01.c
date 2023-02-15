// 该程序做作者用于训练ADT(抽象数据类型)
//  1.建立抽象
//      类型名: 结构数组
//      类型属性:以结构为单位存储的数组
//      类型操作:输入
//              显示所有数据
//              删除
//              查询
//              修改
//              排序
//              存储记录
//  2.建立接口
#include <stdio.h>
#include "list.h"

int main(void)
{
    char ch;//接受菜单选择输入
    int num=0;//监控数组结构中总数列
    DIC user[MAX_NUM];   //创建结构数组
    DIC * point=user;
    while((ch=menu())!='q')
    {
        switch (ch)
        {
            case 'a':add_data(point,num); num++; break;
            case 'b':show_all(point,num);printf("1"); break;
            case 'c':delete_name(point,&num); break;
            case 'd':delete_number(point,&num); break;
            case 'e':search_name(point,num); break;
            case 'f':search_number(point,num); break;
            case 'g':revise_name(point,num);break;
            case 'h':revise_number(point,num);break;
            case 'i':sort(point,num);break;
            case 'k':tofile(point,num);break;
        }
    }
    return 0;
}

