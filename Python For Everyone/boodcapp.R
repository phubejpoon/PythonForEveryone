library(random)

pizza_menu <- c("Cheese Pizza", "Pepperoni Pizza", "Sausage Pizza", "Mushroom Pizza", "Supreme Pizza")

# Define a function to take the customer's order
take_order <- function() {
  customer_order <- list()
  repeat {
    pizza_name <- readline("What kind of pizza would you like? ")
    if (pizza_name %in% pizza_menu) {
      customer_order$pizza_name <- c(customer_order$pizza_name, pizza_name)
      break
    } else {
      print("Sorry, we don't have that kind of pizza.")
    }
  }

  return(customer_order)
}

# Define a function to confirm the customer's order
confirm_order <- function(customer_order) {
  print("Your order is:")
  for (pizza_name in customer_order$pizza_name) {
    print(pizza_name)
  }

  print("Is this correct? (Y/N)")
  confirmation <- readline()

  if (confirmation == "Y") {
    print("Your order is confirmed!")
    return(TRUE)
  } else {
    print("Please re-enter your order.")
    return(FALSE)
  }
}

# Define a function to deliver the customer's order
deliver_order <- function(customer_order) {
  print("Your order is on its way! It will be there in 30 minutes or less.")

  # Simulate a delay
  Sys.sleep(random(1, 30))

  print("Your order has arrived! Enjoy!")
}

# Start the chatbot
print("Welcome to Pizza Delivery AI!")

# Take the customer's order
customer_order <- take_order()

# Confirm the customer's order
if (confirm_order(customer_order)) {
  # Deliver the customer's order
  deliver_order(customer_order)
}
