import React from 'react'
import Axios from 'axios'

export default function Outbreaks() {

    const API = Axios.create({
        baseURL: 'https://disease-watcher.herokuapp.com/',
        headers: {
            'content-type': 'application/json'
        }
    })

    API.get('/outbreak')
        .then((response) => {
            console.log(response)
        })

    


    return (
        <div>
            
        </div>
    )
}
