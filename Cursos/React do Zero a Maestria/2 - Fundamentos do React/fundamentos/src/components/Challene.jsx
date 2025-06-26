const Challenge = () => {
    const a = 1;
    const b = 2;

    return(<div>
        <div>
        <p>A corresponde ao valor de {a}.</p>
        <p>B corresponde ao valor de {b}.</p>
        </div>
        <div>
            <button onClick={() => console.log('A soma de a e b, corresponde a ' + (a + b))}>
            Clique aqui para validar a soma de A e B
            </button>
        </div>
    </div>

    )
}

export default Challenge