describe('Authorization', () => {
    it('Succes Login', () => {
      cy.visit('https://opensource-demo.orangehrmlive.com/')
      cy.get(':nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-input').type('Admin')
      cy.get(':nth-child(3) > .oxd-input-group > :nth-child(2) > .oxd-input').type('admin123')
      cy.get('.oxd-button').click()
      cy.get('.oxd-userdropdown-tab').should('be.visible')
    })
    it('Login with invalid username and password', () => {
      cy.visit('https://opensource-demo.orangehrmlive.com/')
      cy.get(':nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-input').type('sherelia')
      cy.get(':nth-child(3) > .oxd-input-group > :nth-child(2) > .oxd-input').type('sherelia123')
      cy.get('.oxd-button').click()
      cy.get('.oxd-alert').should('be.visible')
    })
  it('Login with invalid username', () => {
      cy.visit('https://opensource-demo.orangehrmlive.com/')
      cy.get(':nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-input').type('sherelia')
      cy.get(':nth-child(3) > .oxd-input-group > :nth-child(2) > .oxd-input').type('admin123')
      cy.get('.oxd-button').click()
      cy.get('.oxd-alert').should('be.visible')
    })
    it('Login with invalid password', () => {
      cy.visit('https://opensource-demo.orangehrmlive.com/')
      cy.get(':nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-input').type('Admin')
      cy.get(':nth-child(3) > .oxd-input-group > :nth-child(2) > .oxd-input').type('sherelia123')
      cy.get('.oxd-button').click()
      cy.get('.oxd-alert').should('be.visible')
    })
    it('Login with empty username and password', () => {
      cy.visit('https://opensource-demo.orangehrmlive.com/')
      cy.get('.oxd-button').click()
      cy.get(':nth-child(2) > .oxd-input-group > .oxd-text').should('be.visible')
      cy.get(':nth-child(3) > .oxd-input-group > .oxd-text').should('be.visible')
    })
    it('Login with empty username', () => {
      cy.visit('https://opensource-demo.orangehrmlive.com/')
      cy.get(':nth-child(3) > .oxd-input-group > :nth-child(2) > .oxd-input').type('admin123')
      cy.get('.oxd-button').click()
      cy.get('.oxd-input-group > .oxd-text').should('be.visible')
    })
    it('Login with empty password', () => {
      cy.visit('https://opensource-demo.orangehrmlive.com/')
      cy.get(':nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-input').type('Admin')
      cy.get('.oxd-button').click()
      cy.get('.oxd-input-group > .oxd-text').should('be.visible')
    })
    
  })