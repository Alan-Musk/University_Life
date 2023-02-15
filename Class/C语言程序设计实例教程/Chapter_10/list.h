#ifndef LIST_H_
#define LIST_H_
#include <stdbool.h>

#define MAX_NUM 20
#define SIZE 20
typedef struct dictionary
{
    char name[SIZE];  //姓名
    long int number;//电话
} DIC;
// 函数原型

// 操作: 给结构数组添加一个项
// 前提条件: user是一个结构数组.n是要添加的下标
// 后置条件: 结构数组中按下标添加了一条数据
bool add_data(DIC * user,int n);

// 操作:显示所有数据
// 前提条件:user是一个结构数组,n是显示总数的下标
void show_all(DIC * user,int n);

// 操作:删除
// 前提条件:user是一个结构数组,已输入数据的总数,由于要删除,所以会产生减一
bool delete_name(DIC * user,int * n);
bool delete_number(DIC * user,int * n);

// 操作:查询
bool search_name(DIC * user,int n);
bool search_number(DIC * user,int n);

// 操作:修改
bool revise_name(DIC * user,int n);
bool revise_number(DIC * user,int n);

// 操作:排序
void sort(DIC * user,int n);

// 操作:向文件输入数据
void tofile(DIC * user,int n);
//非要求函数
//标准输入函数
char * s_gets(char * st,int n);
//清除缓冲区输入
void clean();
//将删除节点后的数组前移
// user是从删除节点开始的地址,n是后面剩余的结构节点
void move_array(DIC * user,int n);
//菜单函数,返回用户选择的一个数
char menu(void);
#endif