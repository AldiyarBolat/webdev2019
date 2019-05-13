import { Component, OnInit } from '@angular/core';
import {TaskList, Task} from '../shared/models/model';
import {ProviderService} from '../shared/services/provider.service';

@Component({
  selector: 'app-viewer',
  templateUrl: './viewer.component.html',
  styleUrls: ['./viewer.component.css']
})

export class ViewerComponent implements OnInit {
  public taskLists: TaskList[] = [];
  public tasks: Task[] = [];
  public name: any = '';
  public logged: boolean = false;
  public login: any = '';
  public password: any = '';

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }

    if(this.logged){
      this.provider.getTaskLists().then(res => {
        this.taskLists = res;
      });
    }
  }
  getTaskOfTaskList(taskList: TaskList) {
    this.provider.getTasksTaskofTaskList(taskList).then(res => {
      this.tasks = res;
    });
  }
  updateTaskList(taskList: TaskList) {
    this.provider.updateTaskList(taskList).then(res => {
      console.log(taskList.name + ' updated');
    });
  }
  deleteTaskList(taskList: TaskList) {
    this.provider.deleteTaskList(taskList).then(res => {
      console.log(taskList.name + ' deleted');
      this.provider.getTaskLists().then(r => {
        this.taskLists = r;
      });
    });
  }
  createTaskList() {
    if (this.name !== '') {
      this.provider.createTaskList(this.name).then(res => {
        this.name = '';
        this.taskLists.push(res);
      });
    }
  }
  auth(){
    if (this.login !== '' && this.password !== '') {
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);

        this.logged = true;
        this.provider.getTaskLists().then(res => {
          this.taskLists = res;
        });

      });
    }
  }
  logout() {
    this.provider.logout().then(res => {
      this.logged = false;
      localStorage.clear();

    });
  }
}
