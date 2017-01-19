resource "aws_db_instance" "foo" {
  storage_encrypted = "True"
  tags {
    Platform = "${var.platform}"
    Name = "${var.platform}_${var.environment}_foo"
    Owner = "${var.owner}"
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
    Owner = "${var.owner}"
    Environment = "${var.environment}"
  }

}
