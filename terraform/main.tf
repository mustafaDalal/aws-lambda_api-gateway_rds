provider "aws" {
  profile = "${var.profile}"
  region = "${var.region}"
}

resource "aws_db_instance" "expenses_db" {
  allocated_storage    = "10"
  db_name              = "{database name}"
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  username             = "{username}"
  password             = "{password}"
  parameter_group_name = "default.mysql8.0"
  skip_final_snapshot  = "true"

}

output "expenses_db_id" {
  value = "${aws_db_instance.expenses_db.identifier}"
}