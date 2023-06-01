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
    char ch;           // 接受菜单选择输入
    int num = 0;       // 监控数组结构中总数列
    DIC user[MAX_NUM]; // 创建结构数组
    DIC *point = user;
    if (openFile(user, &num))
    {
        printf("数据库导出成功!\n");
    }
    else
    {
        printf("数据库导入失败!\n");
    }
    while (ch = menu())
    {
        switch (ch)
        {
        case 1:
            if (add_data(point, num))
            {
                printf("数据添加成功!\n");
                num++;
            }
            break;
        case 2:
            if (revise_number(point, num))
            {
                printf("修改成功!\n");
            }
            else
            {
                printf("修改失败!\n");
            }
            break;
        case 3:
            if(delete_number(point, &num))
            {
                printf("删除成功!\n");
            }
            else
            {
                printf("删除失败!\n");
            }
            break;
        case 4:
            sort(point, num);
            break;
        case 5:
            show_all(point, num);
            break;
        case 6:
            if (!show_person(point, num))
            {
                printf("不存在该学生!\n");
            }
            break;
        case 7:
            if (tofile(point, num))
            {
                printf("文件存储成功!\n");
            }
            else
            {
                printf("文件存储失败!\n");
            }
            break;
        case 8:
            printf("感谢您使用学生管理系统!\n");
            return 0;
        }
        clean();
    }
    return 0;
}
