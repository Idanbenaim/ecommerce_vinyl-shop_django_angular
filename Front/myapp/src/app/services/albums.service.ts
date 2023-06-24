import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Album } from '../components/albums/albums.component';




@Injectable({
  providedIn: 'root'
})
export class AlbumsService {
  MY_SERVER ="http://127.0.0.1:8000/albums";

  constructor(private http: HttpClient) { }

  getAllData(): Observable<Album[]> {
    return this.http.get<any>(this.MY_SERVER)
  }
}
