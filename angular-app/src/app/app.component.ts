import { Component } from '@angular/core';

import { SalesService } from './services/sales.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent{
  title = 'angular-app';

  constructor(
    
    private salesService: SalesService

  ){

    this.salesService.getHelloWorld().subscribe((data)=>{
      console.log(data);
    })

  }

}
