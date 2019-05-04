import { EventEmitter, Injectable } from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import {MainService} from './main.service';
import {TaskList, Task, Token} from '../models/model';


@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {
  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<TaskList[]> {
    return this.get('http://127.0.0.1:8000/api/task_lists',  {});
  }
  createTaskList(namE: any): Promise<TaskList> {
    return this.post('http://127.0.0.1:8000/api/task_lists', {name: namE});
  }
  updateTaskList(taskList: TaskList): Promise<TaskList> {
    return this.put(`http://127.0.0.1:8000/api/task_lists/${taskList.id}`, {name : taskList.name});
  }
  deleteTaskList(taskList: TaskList): Promise<any> {
    return this.delet(`http://127.0.0.1:8000/api/task_lists/${taskList.id}`, {});
  }
  getTasksTaskofTaskList(taskList: TaskList): Promise<Task[]> {
    return this.get(`http://localhost:8000/api/task_lists/${taskList.id}/tasks/`, {});
  }
  // getTaskList(id: number) {
  //   return this.get('http://127.0.0.1:8000/api/task_lists/' + id, {});
  // }



  // createTask(namE: string): Promise<Task> {
  //   return this.post('http://127.0.0.1:8000/api/task_lists', {name: namE});
  // }
  getTasks(): Promise<Task[]> {
    return this.get('http://127.0.0.1:8000/api/tasks', {});
  }
  getTask(id: number): Promise<Task> {
    return this.get('http://127.0.0.1:8000/api/task/' + id, {});
  }
  updateTask(id: number, namee: string) {
    return this.put('http://127.0.0.1:8000/api/task/' + id, {
      name: namee
    });
  }
  deleteTask(id: number) {
    return this.delet('http://127.0.0.1:8000/api/task/' + id, {});
  }



  auth(usernamE: string, passworD: string): Promise<Token> {
    return this.post('http://localhost:8000/api/login/', {
      username: usernamE,
      password: passworD
    });
  }
  logout(): Promise<any> {
    return this.post('http://127.0.0.1:8000/api/logout/', {
    });
  }
}
