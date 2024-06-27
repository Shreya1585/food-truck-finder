provider "aws" {
  region = "us-west-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = ""

  tags = {
    Name = "FoodTruckFinder"
  }
}
