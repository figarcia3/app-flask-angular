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

    this.salesService.get_time_spent_by_day().subscribe((data)=>{
      console.log(data);
    })

  }

}
