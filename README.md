Implementation

Backend - FastAPI:
- api/v1/calculate - supports Core Operations
- api/v2/calculate - supports Additional Operations and Complex Expressions, including operations ordering, (), power, logarithm and sqrt
- api/v3/calculate - the same calculations as in v2 but result is formatted to provide result coloring

Note: A little bit another color schema is used.

Frontend - Bootstrap and Vue3.js
There re two modes in the calculator:
- Basic, where calculation for Core Operations are available, v1 endpoint is used
- Extended, Additional Operations and Complex Expressions can be calculated.
  In this mode v2 endpoint is used if "Color result" not checked and v3 if it checked.

---------------------------------------------------------------------------------------
Calculator Challenge

Overview

This challenge involves creating a web-based calculator application that parforms basic arithmetic operations. The focus is on a robust design that separates business logic from presentation, and is extendable for future
enhancements,

Functional Requirements
1. Core Operations: The calculator must support addition (+), subtraction (=), division (4), and multiplication [*).
2. Client-side Input Format: It takes an operator and two operands as inputs.

94 + 58 = 152

3. REST API Integration: All operations and their results should be accessible via a REST APL.
4, Server-Side Logic: The business logic, including calculations and result processing, must be implemented an the server side
5. Client-Side Presentation: The client-side application should handle only the presentation aspects and interact with the server using AJAX/REST API
6. Multi-Application Support: The REST API should be designed to accommodate multiple client applications without requiring changes to the API contract.

Design and Implementation Standards
1. OOP/0O0D Principles: The application should adhere to Object-Oriented Programming and Design principles
2. Extensibility: Design the application to be open for extensions but closed for madifications (Open/Closed Principle]. This means the core code shouldn't need changes for future extensions.
3. Future Extensions (For Design Consideration Only):
	- Additional Operations (e.g. exponentiation - x~y),
	- Complex Expressions (eg. a + b — e/d + x*d).
	- Varied Result Formats:
		- Simple Numeric Result (e.g. {result:5}).
		- Numeric Result with Calor Coding (e.g. {result:5, color:'red'} ). Color determination is based on the result number's parity (even: green, odd: red).
		Warning - I changed the coloring, RED is used for errors, like division by zero. For EVEN I use PURPLE, for ODD - BLUE
	- The design should account for these potential extensions without implementing them at this stage.

Bonus Challenge: Implement an algorithm that organizes the operators and operands in a specific order.

Implementation Notes
	Ensure that the API and server-side logic are robust and efficient.
	The client-side should be user-friendly and interact seamlessly with the server.

This challange is an opportunity to demonstrate your skills in software design, RESTful API development, and client-server architecture.
