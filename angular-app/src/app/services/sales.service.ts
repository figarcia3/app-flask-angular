import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SalesService {

  constructor(
    private http: HttpClient
  ) {}

  getHelloWorld() {
    return this.http.get("http://127.0.0.1:5000/");
  }
}
