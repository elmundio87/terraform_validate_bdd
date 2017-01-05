resource "aws_db_instance" "foo" {
  storage_encrypted = "True"
  tags {
    Platform = "foo"
    Name = "foo"
    Owner = "bar"
  }
}

resource "aws_instance" "foo" {
  ebs_block_device {
    encrypted = "True"
  }

  tags {
    Platform = "bar"
    Name = "bar"
    Owner = "bar"
  }

}
