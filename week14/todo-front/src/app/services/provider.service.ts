import { EventEmitter, Injectable } from '@angular/core';
import {TaskList, Task, Token} from '../models/models';
import {HttpClient, HttpParams} from '@angular/common/http';
import {MainService} from './main.service';
import * as moment from 'moment';
@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {
  constructor(http: HttpClient) {
    super(http);
  }

  formatDate(date: Date) {
    return moment(date).format('YYYY-MM-DD');
  }

  getTaskLists(sorting = '', search = ''): Promise<TaskList[]> {
    if ( sorting === '') {
      return this.get('http://127.0.0.1:8000/task_lists/?' + 'search=' + search,  {});
    } else {
      return this.get('http://127.0.0.1:8000/task_lists/?' + sorting + '&search=' + search,  {});
    }
  }
  getTasks(id: number, sortBy = '', search = '', filterexp = '') {
    if ( sortBy === '') {
      return this.get(`http://localhost:8000/task_lists/${id}/tasks/?` + 'search=' + search + '&' + filterexp, {});
    } else {
      return this.get(`http://localhost:8000/task_lists/${id}/tasks/?` + 'ordering=' + sortBy + '&search='  + search  + '&' + filterexp, {});
    }
  }
  createTaskList(namE: string): Promise<TaskList> {
    return this.post('http://localhost:8000/task_lists/', {name: namE});
  }
  updateTaskList(taskList: TaskList) {
    return this.put('http://localhost:8000/task_lists/' + taskList.id + '/', {name : taskList.name});
  }

  deleteTaskList(taskList: TaskList) {
    return this.delet('http://localhost:8000/task_lists/' + taskList.id + '/', {});
  }

  updateTask(task: Task) {
    return this.put('http://localhost:8000/task_lists/' + task.task_list.id + '/tasks/' + task.id + '/', {
      name: task.name,
      task_list: task.task_list,
      status: task.status,
      created_at: task.created_at,
      due_on: task.due_on
    });
  }

  createTask(namE: string, statuS: string, createdAt, dueOn, taskList: TaskList) {
      return this.post('http://localhost:8000/task_lists/' + taskList.id + '/tasks/', {
        name: namE,
        status: statuS,
        created_at: this.formatDate(createdAt) + 'T' + '00:00:00',
        due_on: this.formatDate(dueOn) + 'T' + '00:00:00'
      });
  }

  deleteTask(task: Task) {
    return this.delet('http://localhost:8000/task_lists/' + task.task_list.id + '/tasks/' + task.id, {});
  }

  auth(usernamE: string, passworD: string): Promise<Token> {
      return this.post('http://localhost:8000/login/', {
        username: usernamE,
        password: passworD
      });
  }

  logout(): Promise<any> {
    return this.post('http://localhost:8000/logout/', {
    });
  }

}
