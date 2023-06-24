import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AlbumsComponent } from './components/albums/albums.component';
import { ArtistsComponent } from './components/artists/artists.component';
import { MatdesComponent } from './components/matdes/matdes.component';

const routes: Routes = [
    {path:"albums",component:AlbumsComponent},
    {path:"artists",component:ArtistsComponent},
    {path:"mat",component:MatdesComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
