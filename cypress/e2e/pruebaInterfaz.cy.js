describe('Pruebas de logueo en OrangeHRM', () => 
{
    beforeEach(() => {
        cy.visit('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login') //Abre la pagina de Orange HRM antes de ejecutar cada test
    })

    it ('Validar presencia de campos y boton', ()=>{
        cy.contains('h5','Login').should('be.visible') //valida que se visualice el titulo Login
        cy.contains('Username').should('be.visible') //valida la presencia del label username
        cy.contains('Password').should('be.visible') //valida la presencia del label password
        cy.get("input[name='username'][placeholder='Username']").should('be.visible') //valida la presencia del input de username
        cy.get("input[name='password'][placeholder='Password']").should('be.visible') //valida la presencia del input de password
        cy.get("button[type='submit']").should('contain', 'Login') //Valida la presencia del boton de logueo
        cy.get(".orangehrm-login-forgot-header").should('be.visible').and('contain.text','Forgot your password? ') //Valdia presencia del link para cambio de contraseña
        cy.get("a[target='_blank']").should('contain.text','OrangeHRM, Inc') //Valida la presencia del link de OrangeHRM Human Resources
    })

    it('Logueo exitoso', ()=>
        {
        cy.get("input[name='username']").type('Admin') //localiza el input de username e ingresa los valores
        cy.get("input[name='password']").type('admin123') //localiza el input de password e ingresa los valores
        cy.get("button[type='submit']").click() //clic en el boton de login
        cy.get(".oxd-topbar-header-breadcrumb-module").should('contain.text','Dashboard') //Valida que se visualice el titulo Dashboard
    })

    it('Logueo No exitoso', ()=>
        {
        cy.get("input[name='username']").type('Admi') //localiza el input de username e ingresa los valores
        cy.get("input[name='password']").type('admin12') //localiza el input de password e ingresa los valores
        cy.get("button[type='submit']").click() //clic en el boton de login
        cy.contains('.oxd-alert-content-text', 'Invalid credentials').should('be.visible') //Valida que se visualice el mensaje de error
    })
}
)



