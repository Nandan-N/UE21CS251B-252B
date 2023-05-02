#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/sched/task.h>

static void dfs_task_list(struct task_struct *task)
{
    struct task_struct *child;
    struct list_head *list;

    printk(KERN_INFO "Task Name: %s, PID: %d\n", task->comm, task->pid);

    /* DFS: Depth First Search */
    list_for_each(list, &task->children) {
        child = list_entry(list, struct task_struct, sibling);
        dfs_task_list(child);
    }
}

static int __init task_list_init(void)
{
    printk(KERN_INFO "Starting task list kernel module...\n");

    dfs_task_list(&init_task);

    return 0;
}

static void __exit task_list_exit(void)
{
    printk(KERN_INFO "Exiting task list kernel module...\n");
}

module_init(task_list_init);
module_exit(task_list_exit);

MODULE_LICENSE("GPL");