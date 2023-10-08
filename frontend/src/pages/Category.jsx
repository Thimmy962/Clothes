import React, { useEffect, useState } from 'react'

const CategoryPage = ({match}) => {
    const name = match.params.name
    const [categories, setCategories] = useState(null)
    const [products, setProducts] = useState(null)
    const [product, setProduct] = useState(null)
    
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

    let getProducts=async(e)=>{
      let res = await fetch(`http://localhost:8000/items/category/${name}/${e.currentTarget.title}`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json"
        }
      })
      let data = await res.json()
      setProducts(data)
      setProduct(null)
    }

    let getProduct=async(e)=>{
      let res = await fetch(`http://localhost:8000/items/${e.currentTarget.title}`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json"
        }
      })
      let data = await res.json()
      setProduct(data)
      setProducts(null)
      console.log(data)
    }

    if(product){
      return(
        <div id='category'>
        <ul id='categoryList'>
            {categories ? (
              categories.map(category=>(
              <li className='categoryList click subcatclick' onClick={getProducts} key={category.id} title={category.name}>
                  {category.name}</li>
            )))
             : 
            (<h3 className='loading'>Loading</h3>)}
        </ul>
        <div>
                <div>
                  <h1>{product.name}</h1>
                  <h2>{product.category}</h2>
                  <h3>{product.id}</h3>
                  <h4>{product.description}</h4>
                </div>
        </div>
    </div>
      )
    }

  return (
    <div id='category'>
        <ul id='categoryList'>
            {categories ? (
              categories.map(category=>(
              <li className='categoryList click subcatclick' onClick={getProducts} key={category.id} title={category.name}>
                  {category.name}</li>
            )))
             : 
            (<h3 className='loading'>Loading</h3>)}
        </ul>
        <div>
        {products ? (
              products.map(product=>(
              <div className='click' onClick={getProduct} key={product.id} title={product.id}>
                   {product.name}</div>
            )))
             : 
            (<h3 className='loading'>Loading</h3>)}
        </div>
    </div>
  )
}

export default CategoryPage