resource "aws_db_instance" "foo" {
  storage_encrypted = "True"
  tags {
    Platform = "${var.platform}"
    Name = "${var.platform}_${var.environment}_foo"
    Owner = "bar"
    Environment = "${var.environment}"
  }
}

resource "aws_instance" "foo" {
  ebs_block_device {
    encrypted = "True"
  }

  tags {
    Platform = "${var.platform}"
    Name = "${var.platform}_${var.environment}_bar"
    Owner = "bar"
    Environment = "${var.environment}"
  }

}
