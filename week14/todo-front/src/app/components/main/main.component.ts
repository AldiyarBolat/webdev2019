import { Component, OnInit } from '@angular/core';
import {TaskList, Task} from '../../models/models';
import {ProviderService} from '../../services/provider.service';
import * as moment from 'moment';
@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  public taskLists: TaskList[] = [];
  public tasks: Task[] = [];
  public targetTaskList: TaskList;
  public name = '';
  public username = '';
  public password = '';
  public logged = false;
  public taskName = '';
  public taskStatus = '';
  public sorting = '';
  public sortTasks = '';
  public searchTaskList = '';
  public searchTask = '';
  public filterValue = '';
  public filterName = '';
  constructor(private provider: ProviderService) { }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
    if (this.logged) {
      this.provider.getTaskLists().then(res => {
        this.taskLists = res;
      });
    }
  }

  formatDate(date: Date) {
    return moment(date).format('YYYY-MM-DD');
  }

  getTaskOfTaskList(taskList: TaskList) {
    this.targetTaskList = taskList;
    this.provider.getTasks(taskList.id).then(res => {this.tasks = res; });
  }

  createTaskList() {
      if (this.name !== '') {
        this.provider.createTaskList(this.name).then(res => {
          this.name = '';
          this.taskLists.push(res);
        });
      }
  }

  updateTaskList(taskList: TaskList) {
    this.provider.updateTaskList(taskList).then(res => {});
  }

  deleteTaskList(taskList: TaskList) {
    this.provider.deleteTaskList(taskList).then(res => {
      this.provider.getTaskLists().then(r => {
        this.taskLists = r;
      });
    });
  }

  updateTask(task: Task) {
    this.provider.updateTask(task).then(res => {});
  }

  deleteTask(task: Task) {
    this.provider.deleteTask(task).then(res => {
      this.provider.getTasks(task.task_list.id).then(r => {
        this.tasks = r;
      });
    });
  }

  login() {
    if (this.username !== '' && this.password !== '') {
      console.log(this.username);
      console.log(this.password);
      this.provider.auth(this.username, this.password).then(res => {
        console.log(res.token);
        localStorage.setItem('token', res.token);
        this.logged = true;

        this.provider.getTaskLists().then(r => {
          this.taskLists = r;
        });

      });
    }
  }

  logout() {
    this.provider.logout().then(res => {
      localStorage.clear();
      this.logged = false;
    });
  }
  createTask() {
      const createdAt = Date.now();
      const dueOn = Date.now() + (1000 * 60 * 60 * 24);
      if (this.targetTaskList !== undefined) {
        this.provider.createTask(this.taskName, this.taskStatus, createdAt, dueOn, this.targetTaskList).then(res => {
          this.taskName = '';
          this.taskStatus = '';
          this.provider.getTasks(this.targetTaskList.id).then( r => {
            this.tasks = r;
          });
        });
      } else {
        alert('Click to the taskList where you would like to add task!');
      }

  }

  sort() {
      this.provider.getTaskLists(this.sorting, this.searchTaskList).then( res => {
        this.taskLists = res;
      });
  }

  sortingOfTasks() {
    if (this.targetTaskList === undefined) {
      alert('Click to the taskList to see tasks');
    } else {
        this.provider.getTasks(this.targetTaskList.id, this.sortTasks, this.searchTask, this.filterName + '=' + this.filterValue)
          .then(res => {
              this.tasks = res;
          });
    }
  }

}
