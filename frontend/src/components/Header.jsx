import React, { useContext, useEffect, useState } from 'react'
import {Link} from 'react-router-dom'
import AuthContext from '../utils/AuthContext'


const Header = () => {
  const {user, logout} = useContext(AuthContext)
  const [categories, setCategories] = useState(null)

  useEffect(()=>{
    getMenCategory()
  }, [])

  let getMenCategory=async()=>{
      let res = await fetch('http://localhost:8000/items/category', {
        method: "GET",
        headers:{
          "Content-Type": "application/json"
        }
      })
      let data = await res.json()

      setCategories(data)
    }

  return (
    <>
      <div id='header'>
            <Link to='/' className="links click company"><b>CLOTHES</b></Link>
            <div id='loginout'>
            {user ? (
              <div className='smallerDiv'>
                <ul className='category'>
                  {categories && categories.map(category=>(
                    <Link key={category.id} to={`/category/${category.name}`} className='click'><li>{category.name.toUpperCase()}</li></Link>
                  ))}
                </ul>
                <Link to='/' className='click'><h4>{user.username}</h4></Link>
                <h5 onClick={logout} className='click'>Logout</h5>
            </div>
            ) : (
              <div className='smallerDiv'>
                <ul className='category'>
                  {categories && categories.map(category=>(
                    <Link key={category.id} to={`/category/${category.name}`} className='click'><li>{category.name.toUpperCase()}</li></Link>
                  ))}
                </ul>
                <Link to='/login' className="links click">Login</Link>
                <span>|</span>
                <Link to='/register' className="links click">Register</Link>
              </div>
            )
          }
            </div>
      </div>
      <hr />
    </>
  )
    }

export default Header