resource "aws_db_instance" "foo" {
  storage_encrypted = "True"
}

resource "aws_instance" "foo" {
  ebs_block_device {
    encrypted = "True"
  }
}
