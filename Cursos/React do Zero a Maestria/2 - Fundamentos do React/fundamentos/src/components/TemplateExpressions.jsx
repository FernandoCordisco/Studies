const TempleteExpressions = () => {
    
    const name = 'Fernando';
    const data = {
        age: 20,
        job: 'Analista'
    }
    return (
        <div>
            <h1>Olá, {name}. Tudo bem?</h1>
            <p>Você atua como {data.job} e tem {data.age} anos.</p>
            <p>{4+4}</p>
            <p>{console.log('JSX React')}</p>
        </div>
    )
}

export default TempleteExpressions