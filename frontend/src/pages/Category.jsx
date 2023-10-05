import React, { useEffect, useState } from 'react'
import {Link} from 'react-router-dom'

const CategoryPage = ({match}) => {
    const name = match.params.name
    const [categories, setCategories] = useState(null)
    useEffect(()=>{
      getCategory()
    }, [name])
    const getCategory=async()=>{
      let res = await fetch(`http://localhost:8000/items/category/${name}`,{
        method: 'GET',
        headers: {
          "Content-Type": "application/json"
        }
      })
      let data = await res.json()
      setCategories(data)
    }
  return (
    <div id='note'>
        <ul id='categoryList'>
            {categories ? (
              categories.map(category=>(
              <Link className='categoryList' key={category.id} to='/'><li>{category.category} {category.name}</li></Link>
            ))) : (<h3 className='loading'>Loading</h3>)}
        </ul>
    </div>
  )
}

export default CategoryPage