import { List, ListItem } from '@material-ui/core';
import React from 'react';

const songs = [
    {
        name: 'Test Song',
        artist: 'Zed',
        song: [
            { notes: ['F5', 'F6'], delay: 1 },
            { notes: ['F5'], delay: 1 },
            { notes: ['F6'], delay: .5 },
            { notes: ['F5'], delay: 1 },
        ]
    }
]

// TODO:
// show all info, including approximate length?
// Load config info on a per-song basis, but from the database instead of the song's string format
// Add buttons to play once and play on repeat for a given amount of time


// Down the road:
// Allow for songs to be queued for different time slots
// Maybe make the songs play differently based on different data? i.e. weather, stuff like that.
//   Could affect speed or velocity (if that even works)

export default function SongList() {
    return (
        <div>
            <h2>All songs</h2>
            <List>
                {songs.map(song => (
                    <ListItem>
                        {song.name}
                    </ListItem>
                ))}
            </List>
        </div>
    )
}