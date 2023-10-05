import React, { useContext, useEffect, useState } from 'react'
import AuthContext from '../utils/AuthContext'

const HomePage = () => {
  let {tokens, logout} = useContext(AuthContext)
  let [loading, setLoading] = useState(true)
  let [available, setAvailable] = useState(false)

  useEffect(()=>{
  })

  return (
    <div id='homepage'>
      <h1>Hello World</h1>
    </div>
  )
}

export default HomePage