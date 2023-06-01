#ifndef LIST_H_
#define LIST_H_
#include <stdbool.h>
#include <ctype.h>
#define M 3             //M门课
#define MAX_NUM 20      //最多容下20学生
#define SIZE 20         //姓名长度
typedef struct dictionary
{
    int id;//学号
    char name[SIZE];  //姓名
    char gender[SIZE];//性别
    long int number;//电话
    float grades[M];//M门课程
    float total;//总成绩
} DIC;
// 函数原型


// 操作:删除
// 前提条件:user是一个结构数组,已输入数据的总数,由于要删除,所以会产生减一
bool delete_number(DIC * user,int * n);

// 操作:修改
bool revise_number(DIC * user,int n);

// 操作:排序
void sort(DIC * user,int n);

// 操作:向文件输入数据
bool tofile(DIC * user,int n);

//将删除节点后的数组前移
// user是从删除节点开始的地址,n是后面剩余的结构节点
void move_array(DIC * user,int n);


// 操作: 给结构数组添加一个项
// 前提条件: user是一个结构数组.n是要添加的下标
// 后置条件: 为真总数+1,为假不变
bool add_data(DIC * user,int n);

//菜单函数,返回用户选择的一个数
int menu(void);
// 操作:显示所有数据
// 前提条件:user是一个结构数组,n是显示总数的下标
void show_all(DIC * user,int n);

// 操作:按学号输出数据
// 前提条件:user是一个结构数组,n是显示总数的下标
bool show_person(DIC * user,int n);

//清除缓冲区输入
void clean();

// 导入数据库
bool openFile(DIC *user, int *n);
#endif