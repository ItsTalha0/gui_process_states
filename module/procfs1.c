#include<linux/kernel.h>
#include<linux/module.h>
#include<linux/proc_fs.h>
#include<linux/uaccess.h>
#include<linux/version.h>


/* filename for the procfs entry */
#define procfs_name "sample"

static struct proc_dir_entry *our_proc_file;

/* task_struct for tracking the process */
static struct task_struct * my_task_struct;

/* variable for for storing the pid by user */
static int myint=0;
module_param(myint,int,0);

/* function registered for reading the procfs */
static ssize_t procfile_read(struct file *file_pointer,char __user * buffer,size_t buffer_length,loff_t * offset)
{
		long status = -1;
		char s[1000]  ;
		int len = sizeof(s);
		ssize_t ret = len;
		status=my_task_struct->__state | my_task_struct->exit_state;
		s[0]='\0';
		sprintf(s,"%ld",status);
		pr_info("current state is %ld \n",status);
		if( *offset >= len || copy_to_user(buffer,s,len))
		{
				pr_info("copy to user failed\n");
				ret = 0;
		}
		else
		{
				pr_info("procfile read %s\n",file_pointer->f_path.dentry->d_name.name);
				*offset +=len;
		}
		return ret;
}
static const struct proc_ops proc_file_fops = {
		.proc_read = procfile_read,
};

static int __init procfs1_init(void)
{
		our_proc_file = proc_create(procfs_name,0644,NULL,&proc_file_fops);
		if( our_proc_file == NULL )
		{
				proc_remove(our_proc_file);
				pr_alert("Error:could not initialize /proc/%s\n",procfs_name);
				return -ENOMEM;
		}
		/* populating the task_struct for monitoring the process */
		if( myint != 0 )
		{
				my_task_struct = pid_task(find_vpid(myint),PIDTYPE_PID);
				if( my_task_struct != NULL )
						pr_info("/proc/%s %d is pid  %d is current_state %s is name of process created \n",procfs_name,myint,my_task_struct->__state,my_task_struct->comm);
		}
		return 0;
}

int gen_seed()
{
	int i;
	get_random_bytes(&i,1);
	i = i%1000;
	return i;
}


static void __exit procfs1_exit(void)
{
		proc_remove(our_proc_file);
		pr_info("/proc/%s removed\n",procfs_name);
}
static int __init procfs2_init(void)
{
		our_proc_file = proc_create(procfs_name,0644,NULL,&proc_file_fops);
		if( our_proc_file == NULL )
		{
				proc_remove(our_proc_file);
				pr_alert("Error:could not initialize /proc/%s\n",procfs_name);
				return -ENOMEM;
		}
		/* populating the task_struct for monitoring the process */
		if( myint != 0 )
		{
				my_task_struct = pid_task(find_vpid(myint),PIDTYPE_PID);
				if( my_task_struct != NULL )
						pr_info("/proc/%s %d is pid  %d is current_state %s is name of process created \n",procfs_name,myint,my_task_struct->__state,my_task_struct->comm);
		}
		return 0;
}
static int __init procfs3_init(void)
{
		our_proc_file = proc_create(procfs_name,0644,NULL,&proc_file_fops);
		if( our_proc_file == NULL )
		{
				proc_remove(our_proc_file);
				pr_alert("Error:could not initialize /proc/%s\n",procfs_name);
				return -ENOMEM;
		}
		/* populating the task_struct for monitoring the process */
		if( myint != 0 )
		{
				my_task_struct = pid_task(find_vpid(myint),PIDTYPE_PID);
				if( my_task_struct != NULL )
						pr_info("/proc/%s %d is pid  %d is current_state %s is name of process created \n",procfs_name,myint,my_task_struct->__state,my_task_struct->comm);
		}
		return 0;
}
static int __init procfs4_init(void)
{
		our_proc_file = proc_create(procfs_name,0644,NULL,&proc_file_fops);
		if( our_proc_file == NULL )
		{
				proc_remove(our_proc_file);
				pr_alert("Error:could not initialize /proc/%s\n",procfs_name);
				return -ENOMEM;
		}
		/* populating the task_struct for monitoring the process */
		if( myint != 0 )
		{
				my_task_struct = pid_task(find_vpid(myint),PIDTYPE_PID);
				if( my_task_struct != NULL )
						pr_info("/proc/%s %d is pid  %d is current_state %s is name of process created \n",procfs_name,myint,my_task_struct->__state,my_task_struct->comm);
		}
		return 0;
}
module_init(procfs1_init);
module_exit(procfs1_exit);

MODULE_LICENSE("GPL");

